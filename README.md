# Vehicle-Insurance Prediction

Vehicle insurance (also known as car insurance, motor insurance, or auto insurance)
is insurance for cars, trucks, motorcycles, and other road vehicles. Its primary use is to provide
financial protection against physical damage or bodily injury resulting from traffic collisions and
againstliabilitythat could also arise from incidents in a vehicle. Vehicle insurance may
additionally offer financial protection against theft of the vehicle, and against damage to the
vehicle sustained from events other than traffic collisions, such as keying, weather or natural
disasters, and damage sustained by colliding with stationary objects. The specific terms of vehicle
insurance vary with legal regulations in each region.
 It has also been mandated by the government to have an insurance of the vehicle you are driving.
 Hence, we have made this model which, upon deployment is giving us the prediction if the user
 can get an insurance for their vehicle or not.
 

## Dataset

The dataset provided to me has 9 attributes which shall be taken as input from the user. Using our
prediction model over the provided inputs, we are going to predict whether the water is potable or
not with regards to the input provided. The following were the attributes in the given dataset.

<img src="https://github.com/2000utkarsh/Vehicle-Insurance/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.10.35%20PM.png" width="600" height="400" />


## Graphical Depiction of the attributes

<img src="hhttps://github.com/2000utkarsh/Vehicle-Insurance/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.10.39%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.02.48%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Vehicle-Insurance/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.10.42%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Vehicle-Insurance/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.10.45%20PM.png" width="600" height="400" />


## Models Used:

• Decision Tree Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.04%20PM.png" width="500" height="600" />

• Logistic Regression

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.18%20PM.png" width="500" height="600" />

• Random Forest Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.23%20PM.png" width="500" height="600" />

• K-Neighbor Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.31%20PM.png" width="500" height="600" />

• SVC

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.37%20PM.png" width="500" height="600" />

• Multinomial NB

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.49%20PM.png" width="500" height="600" />

## Approach:
During the very first phase of the model, I cleaned the data and made it more sensible in numeric form, i.e. converted all the categorical data to numerical data and removed the NULL and missing values.
In the Second Phase, I did some visualizations over the given dataset which gave me a great view and hints for the implementation of the model.
In the third phase, I implemented various methods over the given dataset, the ones I had mentioned previously. The model gave prediction taking each and every model into consideration and then took out the average value of all the models result and then gave the result which were based on the provided input by the user.
In the final phase, I developed the UI for the model and then linked my model with the created UI for to make it ready for deployment in Django.

## User Interface:

<img src="https://github.com/2000utkarsh/Vehicle-Insurance/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.11.10%20PM.png" width="500" height="400" />

## Output Screen
<img src="https://github.com/2000utkarsh/Vehicle-Insurance/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.11.35%20PM.png" width="500" height="400" />




## Future Scope

In the ever-increasing market of vehicles and the government making stricter rules for the insurance policies of the vehicles, it shall become increasingly necessary for the company to get some efficient and fast way to know whether a person can be given insurance or not. Similarly, it can be used for checking if the person can purchase the vehicle with insurance or not. Hence, the deployed model has got great scope in the near future in the vehicle market.
















