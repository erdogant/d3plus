
Save and Load
''''''''''''''

Saving and loading models is desired as the learning proces of a model for ``d3plus`` can take up to hours.
In order to accomplish this, we created two functions: function :func:`d3plus.save` and function :func:`d3plus.load`
Below we illustrate how to save and load models.


Saving
----------------

Saving a learned model can be done using the function :func:`d3plus.save`:

.. code:: python

    import d3plus

    # Load example data
    X,y_true = d3plus.load_example()

    # Learn model
    model = d3plus.fit_transform(X, y_true, pos_label='bad')

    Save model
    status = d3plus.save(model, 'learned_model_v1')



Loading
----------------------

Loading a learned model can be done using the function :func:`d3plus.load`:

.. code:: python

    import d3plus

    # Load model
    model = d3plus.load(model, 'learned_model_v1')

