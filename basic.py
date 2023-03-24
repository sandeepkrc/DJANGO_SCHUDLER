def fnn():
    """
    function for sending email to
    team every day
    
    """
    print("function running due to the schudler")
    pass
def fdelete():
    """
    function for 
    after 30 day free trail

    """
    print("Function for changeing the status")


from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(fnn, 'interval', seconds=10)
scheduler.start()
