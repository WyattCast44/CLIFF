class Singleton:

    _instance = None

    def __new__(cls):
        """
        Manages the creation of a singleton class
        """

        if cls._instance == None:

            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
