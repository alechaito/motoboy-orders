Motoboy Orders
=====

This is a simple project implemented using python 3.7.


Installing
----------

Install librarys necessary.

.. code-block:: text

    $ pip install -r requirements.txt


Usage
----------------

Run program and you can send motoboy_id to check order associated with him or 0 to check all motoboy orders.

.. code-block:: python

    python main.py

Example of input and output....

Send motoboy_id or 0 to get all or ctrl+c to exit: 0

.. code-block:: python

    Sending orders ... 

    Send motoboy_id or 0 to get all or ctrl+c to exit:0
    Motoboy id : 1, Name: Connie Glueck
    Not received any order...
    Total winned: R$0
    ---------------------------- 

    Motoboy id : 2, Name: Elaine Sanchez
    Received order from store: 3, Value; R$50, Comission: R$9.5
    Total winned: R$9.5
    ---------------------------- 

    Motoboy id : 3, Name: James Rivera
    Received order from store: 2, Value; R$50, Comission: R$4.5
    Received order from store: 2, Value; R$50, Comission: R$4.5
    Total winned: R$9.0
    ---------------------------- 

    Motoboy id : 4, Name: Sarah Grady
    Received order from store: 1, Value; R$50, Comission: R$4.5
    Received order from store: 1, Value; R$50, Comission: R$4.5
    Received order from store: 1, Value; R$50, Comission: R$4.5
    Received order from store: 2, Value; R$50, Comission: R$4.5
    Received order from store: 3, Value; R$50, Comission: R$9.5
    Total winned: R$27.5
    ---------------------------- 

    Motoboy id : 5, Name: Jeffery Koopman
    Received order from store: 2, Value; R$50, Comission: R$5.5
    Received order from store: 3, Value; R$100, Comission: R$18.0
    Total winned: R$23.5
    ---------------------------- 


