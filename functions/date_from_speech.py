from config import *



def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('json_files/token.json'):
        creds = Credentials.from_authorized_user_file('json_files/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'json_files/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('json_files/token.json', 'w') as token:
            token.write(creds.to_json())


    service = build('calendar', 'v3', credentials=creds)
    
    return service 


def get_events(n, service):

    """Calls The calender API.
    Checks and prints out all the upcoming events.
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=n, singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    # Prints the start and name of the next 10 events
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


service = authenticate_google()



def get_date(text):
    """
        Gets user input of a date in the future and checks if there's any upcoming events
    """
    text = text.lower()
    today = datetime.date.today()
    
    if text.count("today") > 0:
        print(today)
        return today
    
    day = -1
    day_of_week = -1
    month = -1
    
    year = today.year
    
    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        
        else:
            for ext in DAY_EXTENTION:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                        
                    except:
                        pass
                    
    if month < today.month and month != -1:
        year = year+1
        
    if day < today.day and month == -1 and day != -1:
        month = month + 1 
        
    if month == -1 and day == -1 and day_of_week != -1:
        curent_day_of_week = today.weekday()
        diff = day_of_week - curent_day_of_week
        
        if diff < 0:
            diff += 7
            if text.count("next") >= 1:
                diff += 7
                
        return today + datetime.timedelta(diff)
    
    return datetime.date(month=month, day=day, year=year) 
    
    

