import logging
from datetime import datetime

class SystemLogger:
    def __init__(self, log_file='logs/system.log'):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        
        # Create logger configuration
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_debug(self, message):
        self.logger.debug(message)

class AuditLogger:
    def __init__(self, audit_file='logs/audit.log'):
        self.audit_file = audit_file
        self.logger = logging.getLogger('audit')
        
        handler = logging.FileHandler(audit_file)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_access(self, user, action, resource, status):
        """Log access attempts"""
        message = f'User: {user} | Action: {action} | Resource: {resource} | Status: {status}'
        self.logger.info(message)

    def log_failed_login(self, username, reason):
        """Log failed login attempts"""
        message = f'Failed Login - Username: {username} | Reason: {reason}'
        self.logger.warning(message)

    def log_mfa_event(self, user, mfa_type, status):
        """Log MFA events"""
        message = f'MFA Event - User: {user} | Type: {mfa_type} | Status: {status}'
        self.logger.info(message)

# Example usage:
# logger = SystemLogger()
# logger.log_info('Application started')
# 
# audit = AuditLogger()
# audit.log_access('john_doe', 'read', '/data/sensitive', 'success')
