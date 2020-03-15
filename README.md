# Computer-Vision---FishEyeManualSitching
Computer Vision - FishEyeManualSitching

Description
===========

このプロジェクトはフィッシュアイレンズ( ~ 8mm)やノーマレンズ(30 ~ 55mm)を使用した映像に適しています。(This code is aimed at stitching images of the FishEyeLens( ~ 8mm), NormalLens(30 ~ 55mm))
----------------------------------------------
このプロジェクトはユーザが直接interactiveしなければなりません。(However, this code must be matched manually, unlike other projects.)
---------------------------------------------
このプロジェクトは、スティッチングが難しい環境でも100%でスティッチングできるように作られているからです。(Because, in any image, we wanted to create a code that would allow us to match features point in the most challenging conditions.)
-----------------------------------------
例えばリピートパターンがたくさんある地下鉄や廊下でのストレッチが可能です。(stitching has always made it possible in subway stations and places with many simple patterns.)
---------------------------------------------------------------
このような環境では、自動ステッチングがエラーになることがあります。(In order to stitch up a difficult image, I thought that interaction with people was a solution.)
-----------------------------------------------------------------------------------------------
手動ステッチングプロジェクトがGitHubになかったため、直接実装しました。(And we've developed it so that you can do manual stitching in the video taken with a regular camera lens, not with fish eye lens.)
-----------------------------------------------------------------------------------------------
もし、結果イメージが気に入らなかったら、ユーザは他のフィーチャーポイントを結び付けて新しい結果を作ることもできます。(If you don't like the stitching of the images, you can match other features point and try again.)
------------------------------------
Use it the way you want.
-----------------------



<hr/>

私がここで作成したコードは、ImageCuttingAndPasteClassとTransformImageClassです。  
クリックした点をカットして写真を貼り付けるClassとTransMatrixを利用して画像を変換させるClassです。


<hr/>  

Normal Lens Process  
----------------
<img src="https://user-images.githubusercontent.com/44941601/76693871-5a637980-66af-11ea-857a-a3a7a165ab85.png" width="300" height="300">
<img src="https://user-images.githubusercontent.com/44941601/76693886-7404c100-66af-11ea-87c4-3ad80c3a9169.png" width="300" height="300">
<img src="https://user-images.githubusercontent.com/44941601/76693905-9696da00-66af-11ea-9e7f-a246b826f212.png" width="300" height="300">
https://youtu.be/rZ_eDzY6PoA
  

Normal Lens Result
------------------
<img src="https://user-images.githubusercontent.com/44941601/76693933-c6de7880-66af-11ea-83d3-a2426c59e62f.png">
https://youtu.be/iz1SKDxUoUQ
  

<hr/>  
 

FishEye Lens Process  
----------------
<img src="https://user-images.githubusercontent.com/44941601/76693793-7dd9f480-66ae-11ea-8b72-1dae71c16933.png" width="300" height="300">
<img src="https://user-images.githubusercontent.com/44941601/76693826-cee9e880-66ae-11ea-80cb-e1b4412798d1.png" width="300" height="300">
<img src="https://user-images.githubusercontent.com/44941601/76693841-e5903f80-66ae-11ea-9e15-378451a87792.png" width="300" height="300">                                                                 
https://youtu.be/6rGAfbwe7Ag
  
<hr/> 

FishEye Lens Result
------------------
<img src="https://user-images.githubusercontent.com/44941601/76693859-2daf6200-66af-11ea-8895-8f9c67799021.png">
https://youtu.be/vqLRw9020yg
  
<hr/> 


  
   
   
   
Python 3.6 OpenCV 3.4.0.0
