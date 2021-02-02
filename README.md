# yolo_data_segmentation

Data Segmentation project by the research group [Human Centered Cyber Physical Production and Assembly Systems (HCCPPAS) of the Institute for Management Sciences - TU Vienna.](https://www.imw.tuwien.ac.at/cps/home/)

This code creates a synthetic dataset for use in training object detection algorithms such as YOLOv3. By using a small number of template images with an arbitrary background, the templates are geometrically transformed and sent to random locations on the arbitrary background by using alpha channel blending. 

The templates are first created using GrabCut in Powerpoint and stored in the templates directory. By providing information on the region of interest in the file name, 
- Label Class
- Object Distance to Camera
- Radius of Circle marking Region of Interest 
- X Coordinate of Circle Centerpoint  
- Y Coordinate of Circle Centerpoint 
- Index (Arbitrary) 

The generated images and corresponding labels are stored in the directory "generated images" and can be used for training of object detection algorithms. 


Authors: 
- Majesa Trimmel 
- Hans Küffner-McCauley 

Questions? Please contact sebastian.schlund@tuwien.ac.at, patrick.rupprecht@tuwien.ac.at


For a detailed description of the ideas underlying the code please look [here](https://github.com/mtrimmel/yolo_data_segmentation/blob/master/docs/proposal-yolo-synthetic.pdf).
