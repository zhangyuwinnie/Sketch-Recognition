# Sketch-Recognition

This is a sketch recognition project. The first part involves feature generation. The raw files are logs containing sketching data of 26 letters. The log consists of a series of sketch points, in the form of points (x,y,t). Thirteen Rubine features[1] were generated from the raw data. The features were generated throught python scripts.

The sencond part is segmentation detecting.The data are from Sketch Recognition Library Database (srlib_db).It's aimed to seperate sketch of multiple strokes into substrokes using corners as the separating point, which is useful for the following shape-recognition. The algorithm of corner finding is Shortstraw.[2] The final accuracy is 0.89.

[1] Rubine, Dean. Specifying gestures by example. Vol. 25. No. 4. ACM, 1991.
[2] Wolin, A., Eoff, B., & Hammond, T. (2008, June). ShortStraw: A Simple and Effective Corner Finder for Polylines. In SBM (pp. 33-40).
