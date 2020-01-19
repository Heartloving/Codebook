# -*- encoding: utf-8 -*-
"""
@Author  : 凡
@Email   : Heartloving515@gmail.com
@File    : DIOU.py
@Time    : 2019/12/31 0:03
@Software: PyCharm
"""

import torch
import torch.nn as nn

from mmdet.core import bbox_overlaps
from ..registry import LOSSES
from .utils import weighted_loss


@weighted_loss
def Diou_loss(pred, target,  eps=1e-3):
    """
    cal DIOU of two boxes or batch boxes
    Computing the DIoU loss between a set of predicted bboxes and target bboxes.
    Args:
        pred (Tensor): Predicted bboxes of format (x1, y1, x2, y2),
            shape (n, 4).
        target (Tensor): Corresponding gt bboxes, shape (n, 4).
        eps (float): Eps to avoid log(0).

    Return:
        Tensor: Loss tensor.
    """
    # cal outer boxes
    outer_left_top = torch.min(pred[:, :2],target[:, :2])
    outer_right_down = torch.max(pred[:, 2:],target[:, 2:])
    outer = outer_right_down - outer_left_top
    outer_diagonal_line = outer[:,0]**2 + outer[:,1]**2

    # cal center distance
    pred_ctr = (pred[:, :2] + pred[:, 2:]) * 0.5
    target_ctr = (target[:, :2] + target[:, 2:]) * 0.5
    ctr_dis = (pred_ctr[:,0]-target_ctr[0])**2 + \
              (pred_ctr[:,1]-target_ctr[1])**2
    # cal diou
    ious = bbox_overlaps(pred, target, is_aligned=True).clamp(min=eps)
    dious = ious - ctr_dis /outer_diagonal_line
    loss = 1-dious
    return loss


@LOSSES.register_module
class DIoULoss(nn.Module):

    def __init__(self, beta=0.2, eps=1e-3, reduction='mean', loss_weight=1.0):
        super(DIoULoss, self).__init__()
        self.beta = beta
        self.eps = eps
        self.reduction = reduction
        self.loss_weight = loss_weight

    def forward(self,
                pred,
                target,
                weight=None,
                avg_factor=None,
                reduction_override=None,
                **kwargs):
        if weight is not None and not torch.any(weight > 0):
            return (pred * weight).sum()  # 0
        assert reduction_override in (None, 'none', 'mean', 'sum')
        reduction = (
            reduction_override if reduction_override else self.reduction)
        loss = self.loss_weight * Diou_loss(
            pred,
            target,
            weight,
            eps=self.eps,
            reduction=reduction,
            avg_factor=avg_factor,
            **kwargs)
        return loss
