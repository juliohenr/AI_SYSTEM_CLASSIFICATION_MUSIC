

        var ctx = document.getElementsByClassName("bar-chart-all-probabilities")

        var lime = document.getElementsByClassName("bar-chart-lime")


        var chartGraph = new Chart(ctx, {

            type:'bar',

            data: {
                labels:["FUNK",
                        "SERTANEJO",
                        "GOSPEL",
                        "BOSSA NOVA"
                        ],

                datasets: [

                    {
                        
                        label:"teste",

                        data: {{ probabilities }},

                 

                     
                        backgroundColor: "#008000"
                    
                    
                    
                    
                    
                    
                    }
                ]

            
            },

        options: {


            title: {

                display:false,
                fontSize:20,
                text: "RELATÓRIO"
            },

            labels: {

                fontStyle: 'bold',

               
                
            },


            legend :{

                display:false
            },

            scales: {
            yAxes: [{
                display: true,
                
                gridLines: {
                    display : false
                   
                },
                ticks: {
                    display: true,
                    fontColor: 'white',
                    beginAtZero:true,
                    fontSize: 20
                }
            }],
            xAxes: [{
                gridLines: {
                    display : false
                },
                ticks: {
                    beginAtZero:true,
                    fontColor: 'white',
                    fontSize: 20
                }
            }]
        },


        


        }


        })







        var chartGraph = new Chart(lime, {

                        type:'bar',

                        data: {
                            labels:["PALAVRA1",
                                    "PALAVRA2",
                                    "PALAVRA3",
                                    "PALAVRA4",
                                    "PALAVRA5"
                                    ],

                            datasets: [

                                {
                                    
                                    label:"teste",

                                    data: [2,2,2,2,2],

                            

                                
                                    backgroundColor: "#008000"
                                
                                
                                
                                
                                
                                
                                }
                            ]


                        },

                        options: {


                        title: {

                            display:false,
                            fontSize:20,
                            text: "RELATÓRIO"
                        },

                        labels: {

                            fontStyle: 'bold',

                        
                            
                        },


                        legend :{

                            display:false
                        },

                        scales: {
                        yAxes: [{
                            display: true,
                            
                            gridLines: {
                                display : false
                            
                            },
                            ticks: {
                                display: true,
                                fontColor: 'white',
                                beginAtZero:true,
                                fontSize: 20
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                display : false
                            },
                            ticks: {
                                beginAtZero:true,
                                fontColor: 'white',
                                fontSize: 20
                            }
                        }]
                        },





                        }


                        })






        new Chart(document.getElementById("doughnut-chart"), {
        type: 'doughnut',
        data: {
     
        datasets: [
            {
            label: "Population (millions)",
            backgroundColor: ["#008000","transparent"],
            borderColor: 'transparent',
            data: {{probability}}
            }
        ]
        },
        options: {
        title: {
            display: false,
            text: 'MEDIUM CONFIDENCE',
            fontStyle: 'bold',
            fontColor:"#008000",
            fontSize:"15"
        },

        legend:{
            display:false
        },
        elements: {
    center: {
      text: 'Red is 2/3 the total numbers',
      color: '#008000', // Default is #000000
      fontStyle: 'Arial', // Default is Arial
      sidePadding: 20, // Default is 20 (as a percentage)
      minFontSize: 20, // Default is 20 (in px), set to false and text will not wrap.
      lineHeight: 25 // Default is 25 (in px), used for when text wraps
    }
  }
        }
    });



