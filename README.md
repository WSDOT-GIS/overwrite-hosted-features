Overwrite Hosted Features
=========================

The Overwrite Hosted Features script can be used to keep the contents of a Feature Collection up to date with information from your source data.

An example of the Overwrite Hosted Features script in use is in the [Transportation 511] viewer, which can by used by departments of transportation to monitor the status of incidents, accidents and roadway conditions.  Transportation 511 services are used to provide content to the Transportation 511 application.  To support variable load, roadway condition data will be exported into a Feature Collection in ArcGIS Online and used in the application configuration.  The Overwrite Hosted Features script can be used to keep the Transportation 511 Feature Collection contents up to date with information from the Incident Management System.

Features
--------

* Use the update script to keep the Feature Collection contents up to date

Requirements
------------

<!-- Start using this this tool now by downloading this repository as a .zip file and unzip to a suitable location or clone the repository with a git tool.  Requirements for using the script include -->
* Python version 2.7.x or version 3.4.  If you are using Python 2.7.8 or earlier, download and install [pip](http://links.esri.com/thirdparty/pipInstall).
* A zipped file geodatabase containing data with which the Feature Collection will be updated
* The URL to your ArcGIS Online Organization, and the username and password for the owner of the feature service and feature collection

For more information on requirements and steps, see [Transportation 511] help.

Setup
-----

### Installation ###

This module can be installed using [pip] using the instructions below.

<!--
These instructions should be updated if Esri registrers this package with PyPI (https://pypi.python.org).
-->

#### Install from GitHub repository URL ####

(If you are not working from Esri's repository, you'll need to modify the repository URL.)

```console
pip install git+https://github.com/Esri/overwrite-hosted-features.git#egg=esri511
```

For more details, see https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support


### Create Configuration ###

Once you have installed the package using [pip], you can generate a configuration file using the follwing command. The configuration file will be created in the current working directory.

```console
update511 --generate-config
```

Usage
-----

    usage: update511 [-h] [--generate-config] [config_file]

    Overwrites hosted features on ArcGIS Online or ArcGIS Portal.

    positional arguments:
    config_file        Path to configuration file. Can be omitted if a
                        overwrite_hosted_features.cfg file exists in the current
                        directory.

    optional arguments:
    -h, --help         show this help message and exit
    --generate-config  Use this flag to generate a
                        "overwrite_hosted_features.cfg" file in the current
                        directory


Resources
---------

Learn more about Esri's [ArcGIS for State Government maps and apps].

Show me a list of other [State Government GitHub repositories].

Additional [information and sample data] are available for the script.

Issues
------

Find a bug or want to request a new feature?  Please let us know by [submitting an issue].

Contributing
------------

Esri welcomes contributions from anyone and everyone.
Please see our [guidelines for contributing].

Licensing
----------

Copyright 2016 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[LICENSE.txt] file.

[Transportation 511]:http://links.esri.com/stategovernment/help/transportation511
[pip]:http://links.esri.com/thirdparty/pipInstall
[ArcGIS for State Government maps and apps]:http://solutions.arcgis.com
[State Government GitHub repositories]:http://esri.github.io/#State-Government
[information and sample data]:http://links.esri.com/stategovernment/help/Transportation511
[guidelines for contributing]:https://github.com/esri/contributing
[LICENSE.txt]:LICENSE.txt
[submitting an issue]:https://github.com/Esri/overwrite-hosted-features/issues

[](Esri Tags: ArcGISSolutions State-Government State Government Transportation 511 Script)
[](Esri Language: Python)
