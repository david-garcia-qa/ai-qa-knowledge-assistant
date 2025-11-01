# MFA Login Specification

When Multi-Factor Authentication (MFA) is enabled for an account:
- After entering email and password, the user must receive a one-time SMS code.
- The one-time code expires after 2 minutes.
- The MFA code cannot be reused.
- If the SMS provider fails, the user may request a single resend.

Account lockout:
- After 3 failed login attempts, the account must be locked for 15 minutes.
- During lockout, further login attempts must be rejected with a clear message.
