def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Welcome to MY DEMO-22"]
