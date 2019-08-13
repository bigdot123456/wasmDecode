from wasm import decode_module
import sys

if __name__ == "__main__":
    print("It's MATRIX World!")
    with open('input-samples/hello/hello.wasm', 'rb') as raw:
        raw1 = raw.read()
        print(raw1)

    mod_iter = iter(decode_module(raw1))
    header, header_data = next(mod_iter)

    for cur_sec, cur_sec_data in mod_iter:
        print(cur_sec_data.get_decoder_meta()['types']['payload'])

    sys.exit()
