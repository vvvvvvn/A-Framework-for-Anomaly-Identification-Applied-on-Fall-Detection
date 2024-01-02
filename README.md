# A Framework for Anomaly Identification Applied on Fall Detection

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
