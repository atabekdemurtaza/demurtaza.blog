
# demurtaza.blog

A brief page to illustrate about my life in particular life.

# Let's start it.

For setup, install these files

*   For **MacOS/Linux** use these line of codes

        virtualenv venv && source venv/bin/activate

*   For **Windows** use these line of codes

        virtualenv --python C:\Path\To\Python\python.exe venv
        .\venv\Scripts\activate

*   After that install dependecies from the *requirements*

        pip install -r requirements/local # for local
        pip install -r requirements/base  # for base
        pip install -r requirements/prod  # for prod


# How to Use the API
Here's how you can use the API provided by this project:

1.**Movie List**: Retrieve a list of movies.

* Endpoint: /list/
* Method: GET

2.**Movie Detail**: Retrieve details of a specific movie.

* Endpoint: /list/<lookup>/
* Method: GET

3.**Stream List**: Retrieve a list of streams.

* Endpoint: /stream/
* Method: GET

To interact with the application, make API requests using the provided endpoints. For example, you can use a tool like curl or a web browser to access the endpoints and retrieve data. Here's an example of how to use curl to make a GET request for the Movie List:

        curl -X GET http://your-api-url/list/


## Author

- [@atabekdemurtaza](https://www.github.com/atabekdemurtaza)


## License

[MIT](LICENSE)



## Logo
![Logo](atabekdemurtaza.jpg)

