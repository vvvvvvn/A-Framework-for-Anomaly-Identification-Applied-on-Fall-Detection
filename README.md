# A Framework for Anomaly Identification Applied on Fall Detection

[Reference](https://github.com/yvesmendes/A-Framework-for-Anomaly-Identification-Applied-on-Fall-Detection/blob/main/pre-proccess.py)

## packages

- `requirements-old.txt` --> 作者原本的
- `requirements.txt` --> 我後來安裝的版本的 （但因為我的 torch 是裝有 cuda12.1 版本的，看要不要直接 python `pre-process.py` 看缺什麼裝什麼？

## Model

- [Get model from st-gcn](https://github.com/yysijie/st-gcn/blob/master/OLD_README.md#get-pretrained-models)

## Data

- [Get UR Video Data From google-drive](https://drive.google.com/file/d/1pfP26WyakGgSRJhhCQ8AqdPgjI_5fSFd/view?usp=drive_link)

- 資料集架構 (部份)

```sh
├── Data/
│   ├── ADLs/
│       ├── adl-01.mp4
│       |   ...
│   ├── Falls/
│       ├── fall-01.mp4
│       |   ...
```

## 執行 `pre-process.py`

- `torchlight` 需另外裝：

```bash=
cd torchlight
python setup.py install
```

- Errors: （都已補上）
  - `FileNotFoundError: [Errno 2] No such file or directory: './config/st_gcn/kinetics-skeleton/demo.yaml'`:
    - 解法： 下載 [此資料夾](https://github.com/yysijie/st-gcn/tree/master/config)
  - ModuleNotFoundError: No module named 'net'
    - 解法： 下載 [此資料夾](https://github.com/yysijie/st-gcn/tree/master/net)
  - FileNotFoundError: [Errno 2] No such file or directory: './resource/kinetics_skeleton/label_name.txt'
    - 解法： 下載 [此資料夾](https://github.com/yysijie/st-gcn/tree/master/resource)
- 改為安裝 `numpy==1.23.5`
