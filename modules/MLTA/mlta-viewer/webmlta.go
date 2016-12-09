package main

import (
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/wcharczuk/go-chart"
	"github.com/zabawaba99/firego"
)

var connectfire *firego.Firebase

//AnalyzerData represents a the format of data contained in firebase
type AnalyzerData struct {
	Author    string    `json:"author"`
	Date      string    `json:"createdAt"`
	Label     string    `json:"label"`
	ModelData ModelData `json:"modelData"`
	ModelType string    `json:"modelType"`
	TestData  TestData  `json:"testData"`
}

//ModelData represents the format of ModelData contained in firebase and AnalyzerData
type ModelData struct {
	HiddenSize string `json:"hiddensize"`
	Predict    string `json:"predict"`
	Predictors string `json:"predicters"`
}

//TestData represents the format of data contained in firebase and AnalyzerData
type TestData struct {
	Score        string `json:"score"`
	Testentries  string `json:"testentries"`
	Testfile     string `json:"testfile"`
	Trainentries string `json:"trainentries"`
	Trainfile    string `json:"trainfile"`
}

//buildGraph:
//input: a list of floats corresponding to the score values from Score in TestData
//input: a list of strings corrsponding to the predictor used to proved the Score from
func buildGraph(yvalues []float64, xvalues []string) {

	f, _ := os.Create("./graphs/graph.png")

	graph := chart.BarChart{
		Height:   512,
		BarWidth: 60,
		XAxis: chart.Style{
			Show: true,
		},
		YAxis: chart.YAxis{
			Style: chart.Style{
				Show: true,
			},
			Range: &chart.ContinuousRange{
				Min: 0.0,
				Max: 100.0,
			},
		},
		Bars: []chart.Value{
			{Value: yvalues[0], Label: xvalues[0]},
			{Value: yvalues[1], Label: xvalues[1]},
		},
	}
	graph.Render(chart.PNG, f)
}

//getXValue
//input: a map of strings to AnalyzerData correspdoing to the testcases of the users
//output: a list of strings corresponding to the predictors used to ttrain models
func getXValue(result map[string]AnalyzerData) []string {

	var xOutput []string
	for _, v := range result {
		xOutput = append(xOutput, v.ModelData.Predictors)
	}

	return xOutput

}

// getYValue
//input: a map of strings to AnalyzerData corrsponding to the test cases of the users
//output: a list of floats correspdonding to the score in TestData
func getYValue(result map[string]AnalyzerData) []float64 {
	var yOutput []float64

	for _, v := range result {
		score, err := strconv.ParseFloat(v.TestData.Score, 64)
		if err != nil {
			panic(err)
		}
		yOutput = append(yOutput, score)
	}

	return yOutput
}

func main() {

	//creates firebase Connection
	connectfire = firego.New("https://machinelearningtestanalyzer.firebaseio.com/", nil)
	connectfire.Auth("B15J822CSDL2aXcApvdEs4comq0e9wIonfkTW0Ed")

	//... the format that the data is in Firebase.
	var data map[string]map[string]map[string]AnalyzerData
	if err :=
		connectfire.Value(&data); err != nil {
		log.Fatal(err)
	}

	//get the x and y vaules for the BarChart
	xvalue := getXValue(data["mlta"]["results"])
	yvalue := getYValue(data["mlta"]["results"])
	buildGraph(yvalue, xvalue)
	http.ListenAndServe(":3000", http.FileServer(http.Dir("./graphs")))

}
