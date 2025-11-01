# QA Notes - High Risk Areas

1. SMS delivery is an external dependency → flaky / slow.
2. MFA code expiry: users get frustrated if the code expires too fast.
3. Lockout workflow is business critical (security). Breaking this = release blocker.
4. We need to confirm that resend is offered only once, not infinite retries.
