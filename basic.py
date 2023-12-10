def send_email():
    """
    function for sending email to
    team every day
    
    """
    print("function running due to the schudler")
    pass
def delete_user():
    """
    function for 
    after 30 day free trail

    """
    print("Function for changeing the status")


from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(fnn, 'interval', seconds=10)
# scheduler.add_job(function_name,'interval',seconds= 40,args=[argument1_of_function,argument2_of_function])
# scheduler.add_job(function_name,args=[argument1_of_function,argument2_of_function],trigger='cron', minute=1)
scheduler.start()
