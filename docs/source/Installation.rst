Installation
################

Create environment
**********************

If desired, install ``d3plus`` from an isolated Python environment using conda:

.. code-block:: python

    conda create -n env_d3plus python=3.8
    conda activate env_d3plus


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install d3plus

    # Force update to latest version
    pip install -U d3plus


Github source
************************************

.. code-block:: console

    # Install directly from github
    pip install git+https://github.com/erdogant/d3plus


Uninstalling
################

Remove environment
**********************

.. code-block:: console

   # List all the active environments. d3plus should be listed.
   conda env list

   # Remove the d3plus environment
   conda env remove --name d3plus

   # List all the active environments. d3plus should be absent.
   conda env list


Remove installation
**********************

Note that the removal of the environment will also remove the ``d3plus`` installation.

.. code-block:: console

    # Install from Pypi:
    pip uninstall d3plus

