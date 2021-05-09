cd ..;
cd Instances;
for FILE in *.dat; 
do
    time gtimeout 2h glpsol -m ../GLPK/GraphColoringGLPK.mod -d $FILE -o ../sol/$FILE.sol >> ../GLPK/Outputs/$FILE.out;
    echo $FILE;
done