# Audit / Compliance Requirements

All authentication attempts must be logged for audit:
- timestamp (UTC),
- user identifier,
- outcome: SUCCESS, BAD_PASSWORD, MFA_FAILED, LOCKED_OUT.

Audit logs must be exportable for security review.
Audit logs must be retained for at least 180 days.
