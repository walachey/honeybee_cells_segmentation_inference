config_default = {
    "random_seed": 123,
    "dataloader": {"batch_size": 4, "pin_memory": True, "num_workers": 8, "drop_last": False},
    "sliding_window_inferer": {"roi_size": 512, "overlap": 0.4, "mode": "gaussian"},
}


label_classes_default = [
    {"id": "8af029f5-14d3-431a-aedf-754a4f71a9aa", "color": "#7cb43cd9", "png_index": 1, "name": "bees"},
    {"id": "34221592-4595-4cf2-82e6-d0631c02d030", "color": "#e5d4f69c", "png_index": 2, "name": "empty_cell"},
    {"id": "0fbeb702-db66-478d-ae1e-3f20a5aaa4b3", "color": "#8cbef891", "png_index": 3, "name": "open_brood"},
    {"id": "0bfbb78b-26b3-4b89-a7a0-8db2840561b6", "color": "#fff4748a", "png_index": 4, "name": "open_honey"},
    {"id": "69f9b64b-a314-49fb-ad37-961ac05bdd25", "color": "#f5d03ae0", "png_index": 5, "name": "capped_honey"},
    {"id": "20184ab5-13d3-452d-8443-cee83fff74bf", "color": "#1e5faadb", "png_index": 6, "name": "capped_brood"},
    {"id": "243a2a98-3a93-467f-ad01-5afc05c14a07", "color": "#9c3eeba8", "png_index": 7, "name": "pollen"},
    {"id": "d5c56ea1-1ec0-4873-b0d4-c94c8627e6fe", "color": "#417505b3", "png_index": 8, "name": "bee_in_cell"},
]
