# Application Class

## Config

When you initilize the `Application` class, you have the option of passing a dictionary which will be merged with the default application configuration. You can pass any value into the application, if the key already exists it will be updated with your value. A list of default configuration keys and values can be found below.

| Key                 | Default Value              |
|---------------------|----------------------------|
| name                | Console Application        |
| version             | 1.0.0                      |
| description         | Helping you build CLI apps |
| env                 | dev                        |
| width               | 55                         |
| strict_registration | False                      |