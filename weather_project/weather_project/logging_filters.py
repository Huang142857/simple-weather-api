import logging

class AddRequestContextFilter(logging.Filter):
    def filter(self, record):
        record.user_id = 'anonymous'
        record.path_info = '-'
        record.request_method = '-'
        record.status_code = '-'
        if hasattr(record, 'request'):
            request = record.request

            record.user_id = request.user.id if request.user.is_authenticated else 'anonymous'
 
            record.path_info = request.path_info
 
            record.request_method = request.method
        if hasattr(record, 'status_code'):
            record.status_code = record.status_code
        
        return True