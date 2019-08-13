from wasm import *
import sys

if __name__ == "__main__":
    print("It's MATRIX World!")
    with open('input-samples/hello/hello.wasm', 'rb') as raw:
        raw1 = raw.read()
        # print(raw1)

    mod_iter = iter(decode_module(raw1))
    header, header_data = next(mod_iter)

    for cur_sec, cur_sec_data in mod_iter:
        if cur_sec_data.id == SEC_GLOBAL:
            print("GlobalSection:")
            for idx, entry in enumerate(cur_sec_data.payload.globals):
                print(
                    format_mutability(entry.type.mutability),
                    format_lang_type(entry.type.content_type),
                )

                for cur_insn in entry.init:
                    print(format_instruction(cur_insn))

        if cur_sec_data.id == SEC_ELEMENT:
            print("ElementSection:")
            for idx, entry in enumerate(cur_sec_data.payload.entries):
                print(entry.index, entry.num_elem, entry.elems)
                for cur_insn in entry.offset:
                    print(format_instruction(cur_insn))

        if cur_sec_data.id == SEC_DATA:
            print("DataSection:")
            for idx, entry in enumerate(cur_sec_data.payload.entries):
                print(entry.index, entry.size, entry.data.tobytes())
                for cur_insn in entry.offset:
                    print(format_instruction(cur_insn))

    sys.exit()
