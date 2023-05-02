## Overview
This fitness management application aims to achive below taksks:
1. Enabling gym administrators to have better management of the gym
2. Helping trainers manage their customers and workout sessions
3. Allowing gym members to have access to their workout plans, workouts, and nutrition plans easily

## ER Diagram

![ER Diagram](https://user-images.githubusercontent.com/73263355/235767261-dee9dbb7-bc94-4a1b-88a5-6d7d7369df20.jpg)

## Authentication and Authorization Scheme
Permission/Group	wi_user	wi_admin	wi_trainer	SuperUser
Workout Plan				
   View	X	X	X	X
   Add		X	X	X
   Change		X	X	X
   Delete		X	X	X
				
Nutrition Plan				
   View	X	X	X	X
   Add		X	X	X
   Change		X	X	X
   Delete		X	X	X
				
Membership				
   View	X	X	X	X
   Add		X		X
   Change		X		X
   Delete		X		X
				
Payment				
   View	X	X	X	X
   Add		X		X
   Change		X		X
   Delete		X		X
				
Member				
   View	X	X	X	X
   Add		X		X
   Change		X		X
   Delete		X		X
				
Trainer				
   View	X	X	X	X
   Add		X		X
   Change		X		X
   Delete		X		X
				
Workout				
   View	X	X	X	X
   Add		X	X	X
   Change		X	X	X
   Delete		X	X	X![image](https://user-images.githubusercontent.com/73263355/235767606-f57b0f8d-c30c-407d-99de-3eebd56ac445.png)

