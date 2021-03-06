import os.path
from dipy.data.fetcher import fetch_data


def get():
    pth = os.path.abspath('.')

    url = 'https://digital.lib.washington.edu/researchworks/bitstream/handle/1773/38475/'
    hardi_data = {
        'dwi.nii.gz': (url+'HARDI193.nii.gz','0b735e8f16695a37bfbd66aab136eb66'),
        'bval.txt': (url+'HARDI193.bval', 'e9b9bb56252503ea49d31fb30a0ac637'),
        'bvec.txt': (url+'HARDI193.bvec', '0c83f7e8b917cd677ad58a078658ebb7')}

    fetch_data (hardi_data, os.path.join(pth, 'sherbrooke_3shell'))
