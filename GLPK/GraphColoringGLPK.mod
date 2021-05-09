/* Parameters: number of vertexs */
param vertexCount;

/* set V = vertex list */
set V;
set E within (V cross V);

/* Decision variables */
var y{V} binary;   /* If color h is on solution */
/*var x{E} binary;  */  /* If vertex received color h */
var x{i in V, j in V} binary;

/* Objective function */
minimize colors_count: sum {i in V} y[i];

/* Every vertex receives one and only one color */
s.t. R1 {i in V}: 
    sum {h in V} x[i,h] = 1; 

/* Two connected vertex don't have the same color */
s.t. R2 {(i, j) in E, h in V}:
    x[i,h] + x[j,h] <= y[h];


/* We use the first colors the most we can */
s.t. R3 {h in V: h < vertexCount}: 
    sum{i in V} x[i,h] >= sum{i in V} x[i,h+1]; 

