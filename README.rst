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
    Motoboy id: 1,         Name: Ashley Paradis,         TotalWin: 0         
    Not received any order...
    ---------------------------- 

    Motoboy id: 2,         Name: Ellen Reilly,         TotalWin: 9.5         
    Store ID    Order Value    Comission
    ----------  -------------  -----------
            3             50          9.5
    ---------------------------- 

    Motoboy id: 3,         Name: Teresa Carter,         TotalWin: 9.0         
    Store ID    Order Value    Comission
    ----------  -------------  -----------
            2             50          4.5
            2             50          4.5
    ---------------------------- 

    Motoboy id: 4,         Name: Kevin Jones,         TotalWin: 30.5         
    Store ID    Order Value    Comission
    ----------  -------------  -----------
            1             50          4.5
            1             50          4.5
            1             50          4.5
            3            100         17
    ---------------------------- 

    Motoboy id: 5,         Name: Marilyn Lee,         TotalWin: 21.5         
    Store ID    Order Value    Comission
    ----------  -------------  -----------
            2             50          5.5
            2             50          5.5
            3             50         10.5
    ---------------------------- 


