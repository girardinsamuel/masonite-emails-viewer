from masonite.routes import Get, Post

ROUTES = [
    # emails app
    Get('/emails', 'EmailsController@index').name('emails'),
    Get('/emails/@name', 'EmailsController@detail').name('emails.detail'),
    Post('/emails/@name/send', 'EmailsController@send').name('emails.send'),
]

