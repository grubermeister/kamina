import sys, logging


level_debug = logging.DEBUG
level_info  = logging.INFO
level_error = logging.ERROR


def hire(name, debug=False, fmt='', logfile='', syslog=''):
    if not fmt:
        if debug or syslog or logfile:  
            fmt = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        else:
            fmt = "%(message)s"
        
    log = logging.getLogger(name)
    formatter = logging.Formatter(fmt)
    if debug:  log.setLevel(level_debug)
    else:  log.setLevel(level_info)
        
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

    if logfile:  
        file_handler = logging.FileHandler(logfile,"a")
            
        if debug:  file_handler.setLevel(level_debug)
        else:  file_handler.setLevel(level_error)
            
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

    return log
