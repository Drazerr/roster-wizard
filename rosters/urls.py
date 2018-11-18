from django.urls import path

from .views import (
    LeaveListView,
    LeaveUpdateView,
    LeaveDetailView,
    LeaveDeleteView,
    LeaveCreateView,
    RoleListView,
    RoleUpdateView,
    RoleDetailView,
    RoleDeleteView,
    RoleCreateView,
    ShiftListView,
    ShiftUpdateView,
    ShiftDetailView,
    ShiftDeleteView,
    ShiftCreateView,
    ShiftRuleListView,
    ShiftRuleUpdateView,
    ShiftRuleDetailView,
    ShiftRuleDeleteView,
    ShiftRuleCreateView,
    ShiftRuleRoleListView,
    ShiftRuleRoleUpdateView,
    ShiftRuleRoleDetailView,
    ShiftRuleRoleDeleteView,
    ShiftRuleRoleCreateView,
    StaffRuleListView,
    StaffRuleUpdateView,
    StaffRuleDetailView,
    StaffRuleDeleteView,
    StaffRuleCreateView,
    TimeSlotListView,
    TimeSlotUpdateView,
    TimeSlotDetailView,
    TimeSlotDeleteView,
    TimeSlotCreateView,
)

urlpatterns = [
    path("leave/<int:pk>/edit/", LeaveUpdateView.as_view(), name="leave_edit"),
    path("leave/<int:pk>/", LeaveDetailView.as_view(), name="leave_detail"),
    path(
        "leave/<int:pk>/delete/",
        LeaveDeleteView.as_view(),
        name="leave_delete",
    ),
    path("leave/new/", LeaveCreateView.as_view(), name="leave_new"),
    path("leave/", LeaveListView.as_view(), name="leave_list"),
    path("role/<int:pk>/edit/", RoleUpdateView.as_view(), name="role_edit"),
    path("role/<int:pk>/", RoleDetailView.as_view(), name="role_detail"),
    path(
        "role/<int:pk>/delete/", RoleDeleteView.as_view(), name="role_delete"
    ),
    path("role/new/", RoleCreateView.as_view(), name="role_new"),
    path("role/", RoleListView.as_view(), name="role_list"),
    path("shift/<int:pk>/edit/", ShiftUpdateView.as_view(), name="shift_edit"),
    path("shift/<int:pk>/", ShiftDetailView.as_view(), name="shift_detail"),
    path(
        "shift/<int:pk>/delete/",
        ShiftDeleteView.as_view(),
        name="shift_delete",
    ),
    path("shift/new/", ShiftCreateView.as_view(), name="shift_new"),
    path("shift/", ShiftListView.as_view(), name="shift_list"),
    path(
        "shiftrule/<int:pk>/edit/",
        ShiftRuleUpdateView.as_view(),
        name="shift_rule_edit",
    ),
    path(
        "shiftrule/<int:pk>/",
        ShiftRuleDetailView.as_view(),
        name="shift_rule_detail",
    ),
    path(
        "shiftrule/<int:pk>/delete/",
        ShiftRuleDeleteView.as_view(),
        name="shift_rule_delete",
    ),
    path(
        "shiftrule/new/", ShiftRuleCreateView.as_view(), name="shift_rule_new"
    ),
    path("shiftrule/", ShiftRuleListView.as_view(), name="shift_rule_list"),
    path(
        "shiftrulerole/<int:pk>/edit/",
        ShiftRuleRoleUpdateView.as_view(),
        name="shift_rule_role_edit",
    ),
    path(
        "shiftrulerole/<int:pk>/",
        ShiftRuleRoleDetailView.as_view(),
        name="shift_rule_role_detail",
    ),
    path(
        "shiftrulerole/<int:pk>/delete/",
        ShiftRuleRoleDeleteView.as_view(),
        name="shift_rule_role_delete",
    ),
    path(
        "shiftrulerole/<slug:shiftrule>/new/",
        ShiftRuleRoleCreateView.as_view(),
        name="shift_rule_role_new",
    ),
    path(
        "shiftrulerole/",
        ShiftRuleRoleListView.as_view(),
        name="shift_rule_role_list",
    ),
    path(
        "leave/<int:pk>/edit/",
        StaffRuleUpdateView.as_view(),
        name="staff_rule_edit",
    ),
    path(
        "staffrule/<int:pk>/",
        StaffRuleDetailView.as_view(),
        name="staff_rule_detail",
    ),
    path(
        "staffrule/<int:pk>/delete/",
        StaffRuleDeleteView.as_view(),
        name="staff_rule_delete",
    ),
    path(
        "staffrule/new/", StaffRuleCreateView.as_view(), name="staff_rule_new"
    ),
    path("staffrule/", StaffRuleListView.as_view(), name="staff_rule_list"),
    path(
        "timeslot/<int:pk>/edit/",
        TimeSlotUpdateView.as_view(),
        name="timeslot_edit",
    ),
    path(
        "timeslot/<int:pk>/",
        TimeSlotDetailView.as_view(),
        name="timeslot_detail",
    ),
    path(
        "timeslot/<int:pk>/delete/",
        TimeSlotDeleteView.as_view(),
        name="timeslot_delete",
    ),
    path("timeslot/new/", TimeSlotCreateView.as_view(), name="timeslot_new"),
    path("timeslot/", TimeSlotListView.as_view(), name="timeslot_list"),
]
