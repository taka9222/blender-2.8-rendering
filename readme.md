### Contents
config_samples : samples of config.ini files <br>
misc/BSDF_Test : output images with various Principles BSDF parameters <br>
misc/directional2euler.py : script to convert space-separated directional vector to comma-separated XYZ-euler angle <br> 
misc/viewnpy.py : script to view npy images <br>
output_samples : output samples of Bunny and Sphere <br>
working_dir : object file, light data, view data, texture and HDRI <br>
config_tutorial.txt : usage of config settings <br>
render_object.py : script that can run with command line <br>

### Tutorial
Blender がカスタムビルドされている場所(C:\blender-git\build_windows_x64_vc16_Release\bin\Release等)で以下のコマンドにより実行できます．
```
> blender.exe -b -P render_object.py config.ini (複数可)
```
Blender のカスタムビルドの具体的な方法は https://wiki.blender.org/wiki/Building_Blender を参考にして，ビルド前にソースの一部を書き換える必要があります．ソースの変更箇所としては以下の2点です．
```
ソース source/blender/compositor/operations/COM_ViewerOperation.h 内 58行目
bool isOutputOperation(bool /*rendering*/) const { 
    if (G.background) return false; return isActiveViewerOutput(); }
を以下に変更
bool isOutputOperation(bool /*rendering*/) const {return isActiveViewerOutput(); }
```
```
ソース source/blender/compositor/operations/COM_PreviewOperation.h 内 48行目
bool isOutputOperation(bool /*rendering*/) const { return !G.background; }
を以下に変更
bool isOutputOperation(bool /*rendering*/) const { return true; }
```

### Dockerfile について
```
docker build -t repo-luna.ist.osaka-u.ac.jp:5000/enomoto/blender_2.8_rendering:latest -f Dockerfile .
docker run --rm -itd --name=blender -v /mnt/workspace2019:/mnt/workspace2019 -v /path/to/blender_2.8_rendering:/path/to/blender_2.8_rendering repo-luna.ist.osaka-u.ac.jp:5000/enomoto/blender_2.8_rendering:latest
docker exec -it blender bash
```
```
docker push repo-luna.ist.osaka-u.ac.jp:5000/enomoto/blender_2.8_rendering:latest
docker pull repo-luna.ist.osaka-u.ac.jp:5000/enomoto/blender_2.8_rendering:latest
```