.. sectnum::

===============================================================================
Quoter Bot
===============================================================================
:Author: `Ignacio Talavera Cepeda <https://github.com/ignacioct>`_

This is a Twitter Bot inspired on `Vita & Virgina Bot <https://twitter.com/VitaVirginiaBot>` 
which tweets a quote from a random .txt files inside the lyrics folder. 
In those files, each quote must start with a '$' symbol and end with a '%' symbol, like
in the following example:

.. code:: 

   $The great revelation perhaps never did come. 
   Instead, there were little daily miracles, illuminations, matches struck unexpectedly in the dark; 
   here was one.%

Keys are store in a 'keys.py' file in the same directory as the main script, and it must have this structure

.. code:: 

   consumer_key = '123456'
    consumer_secret = '654321'
    access_token = '13579'
    access_token_secret = '24680'

