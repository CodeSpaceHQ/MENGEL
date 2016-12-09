# MLTA Viewer
###### Machine Learning Test Analyzer Graphical output
The MLTA Viewer tool is used to view, in a graphical way, output from the machine learning algorithms
In its current form it will only graph predictor vs. the score produced using that predictor.

## Getting Started
### Before You Begin
Make sure you have properly installed [golang](https://golang.org/doc/install)

### Other packages needed when installing
#### Packages
If you have go installed correctly you can install the package using this command:

[go-chart](github.com/wcharczuk/go-chart)

```bash
go get github.com/wcharczuk/go-chart
```
[firego](github.com/zabawaba99/firego)

```bash
go get github.com/zabawaba99/firego
```

### Usage
Currently, in order to run the MLTA viewer locally you must navigate to the MLTA Viewer folder. Run the following command:

```bash
go run webmlta.go
```

Once the `webmlta.go` file is running, navigate to your browser and in the URL type _localhost:3000_.  A file browser should appear with with one file entitled _graph.png_  
