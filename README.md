# d3plus

[![Python](https://img.shields.io/pypi/pyversions/d3plus)](https://img.shields.io/pypi/pyversions/d3plus)
[![Pypi](https://img.shields.io/pypi/v/d3plus)](https://pypi.org/project/d3plus/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/d3plus/)
[![LOC](https://sloc.xyz/github/erdogant/d3plus/?category=code)](https://github.com/erdogant/d3plus/)
[![Downloads](https://static.pepy.tech/personalized-badge/d3plus?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/d3plus)
[![Downloads](https://static.pepy.tech/personalized-badge/d3plus?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/d3plus)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/d3plus/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/d3plus.svg)](https://github.com/erdogant/d3plus/network)
[![Issues](https://img.shields.io/github/issues/erdogant/d3plus.svg)](https://github.com/erdogant/d3plus/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![DOI](https://zenodo.org/badge/228166657.svg)](https://zenodo.org/badge/latestdoi/228166657)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://towardsdatascience.com/what-are-d3plus-loadings-and-biplots-9a7897f2e559)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg?logo=github%20sponsors)](https://erdogant.github.io/d3plus/pages/html/Documentation.html#colab-notebook)
![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/d3plus)
![GitHub repo size](https://img.shields.io/github/repo-size/erdogant/d3plus)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://erdogant.github.io/d3plus/pages/html/Documentation.html#)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->





<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``d3plus`` is Python package

# 
**Star this repo if you like it! ⭐️**
#


## Blog/Documentation

* [**d3plus documentation pages (Sphinx)**](https://erdogant.github.io/d3plus/)
* [**Notebook with examples**](https://colab.research.google.com/github/erdogant/d3plus/blob/master/notebooks/d3plus.ipynb)
* [**Read more details and usage about d3plus in this blog!**](https://towardsdatascience.com/d3plus)

* <a href="https://erdogant.github.io/d3plus/"> <img src="https://img.shields.io/badge/Sphinx-Docs-Green" alt="Open documentation pages"/> </a> d3plus documentation pages 
* <a href="https://colab.research.google.com/github/erdogant/d3plus/blob/master/notebooks/d3plus.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open example In Colab"/> </a> Notebook example 
* <a href="https://towardsdatascience.com/a-step-by-step-guide-for-clustering-images-4b45f9906128"> <img src="https://img.shields.io/badge/Medium-Blog-blue" alt="Open Blog"/> </a> Blog: A step-by-step guide for clustering images 


### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install d3plus from PyPI (recommended). d3plus is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_d3plus python=3.8
conda activate env_d3plus
```

```bash
pip install d3plus            # normal install
pip install --upgrade d3plus # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/erdogant/d3plus.git@0.1.0#egg=master
pip install git+https://github.com/erdogant/d3plus#egg=master
pip install git+https://github.com/erdogant/d3plus

# By cloning
git clone https://github.com/erdogant/d3plus.git
cd d3plus
pip install -U .
```  

#### Import d3plus package
```python
import d3plus as d3plus
```

#### Example:
```python
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/d3plus/data/example_data.csv')
model = d3plus.fit(df)
G = d3plus.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/d3plus/blob/master/docs/figs/fig1.png" width="600" />
  
</p>


#### References
* https://github.com/erdogant/d3plus

#### Citation
Please cite in your publications if this is useful for your research (see citation).
   
### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
