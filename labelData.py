import numpy as np
import matplotlib.pyplot as plt
import glob


def main(args):

    ninput = len(glob.glob(f'{args.input}/picture*'))
    
    labels = []

    for i in range(ninput):
        try:
            with open(f'{args.input}/picture_{i}.npy', 'rb') as f:
                data = np.load(f)
            plt.imshow(data, cmap=plt.get_cmap('gray'))
            plt.ion()
            plt.show()
            print(f'picture {i}')
            label = ''
            while label == '' or label not in args.classes:
                print('Enter the label:')
                label = input()
            labels.append(label)
            plt.close()
        except:
            print(f'{args.input}/picture_{i}.npy not found!')

    labels = np.array(labels)
    with open(f'{args.input}/labels.npy', 'wb') as f:
        np.save(f, labels)


    

if __name__ == '__main__':
    from argparse import ArgumentParser
    from argparse import ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description='Script to label images.', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input', '-i', type=str, help='Path to input')
    parser.add_argument('--classes', '-c', nargs='*', default=['0','1','2'], help='Allowed classes')
    args = parser.parse_args()
        
    main(args)
