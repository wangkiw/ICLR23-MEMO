from models.memo import MEMO

def get_model(model_name, args):
    name = model_name.lower()
    if name == 'memo':
        return MEMO(args)
    else:
        assert 0
