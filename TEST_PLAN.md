Test home:
    Send a request to the home view and check type of response.
    Send a GET request to the home view with no DB returns no posts.
    Send a GET request to the home page, and ensure it has the correct amount of blog posts when connected to DB.
    send a GET request to the home view and ensure it responds with the correct route, and a list of blog posts.
    Send a GET request to the home page, and ensure it has the correct content we wish to see and the correct amount of posts.

Test detail:
    Send a request to the detail view and check type of response.
    Send GET request (with ID) to detail view, and ensure it returns the proper post.
    Send GET request (with ID) to the detail URL. Ensure that it has the proper content we wish to see.
    Send GET request with bad ID returns proper error/redirects to 404 page.

Test create:
    Send a request to the create view and check type of response.
    Send a GET request to create url, ensure that we see the proper content.
    Send a POST with incomplete data returns incomplete data back on create page.
    Send a POST request to create view. Ensure that new entry is represented in postgres database.
    Send a POST request to create URL. Ensure that it gets redirected to homepage, and that home page now has the new entry at the top.

Test edit:
    Send a request to the edit view and check type of response.
    Send multiple GET requests (with IDs) to edit view, and ensure it returns the proper post each time.
    Send multiple GET requests (with IDs) to the edit URL. Ensure that the URL has the correct  content.
    Send a POST request to the edit view, ensure that the postgres database has not changed size, and that the newly edited entry has changed.
    Send a POST request to the edit URL, ensure that it redirects to the detail view, and that the newly edited post is displayed on it.
    Send GET request with bad ID returns proper error/redirects to 404 page.

Test DB:
    Test that when models are added to DB the DB has entries.
    Test an entry in the DB can be viewed after adding.