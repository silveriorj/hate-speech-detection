from torch.utils.data import Dataset, DataLoader
import torch

class HateSpeechDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length=512):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.encoded_texts = []
        self.__encode__()
        
    def __encode__(self):
        for text in self.texts:
            encoding = self.tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=self.max_length,
                padding='max_length',
                truncation=True,
                return_attention_mask=True,
                return_token_type_ids=False,
                return_tensors='pt'
            )
            self.encoded_texts.append(encoding)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        return {
            'input_ids': self.encoded_texts[idx]['input_ids'].flatten(),
            'attention_mask': self.encoded_texts[idx]['attention_mask'].flatten(),
            'labels': torch.FloatTensor(self.labels[idx]),
        }
