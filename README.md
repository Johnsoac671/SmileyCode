# SmileyCode
An Emoji-based programming language

Brief overview (subject to change):

start_symbol                                                                🙂

variable declaration
    declaration_symbol type name = value end_symbol                         📝 type name 🟰 value 🚫
    
    string                                                                  🧵
    integer                                                                 🧮
    float                                                                   🎳
    boolean                                                                 👻 ✅ | ❌
    array                                                                   📁 type, ➡️val0, val1, val2, ...⬅️

    call variable                                                           💡variable name

comments
    comment body                                                            💭 this is a comment 💭

functions
    declaration func_symbol name args = body return end_symbol 📝 ⚙️ name ⏩arg1, arg2, etc⏪ 🟰 ⏭️ ... ⏮️ ↩️ return_value🚫
    func_symbol name args                                                   ⚙️ name ⏩arg1, arg2, etc⏪ 🚫, ⚙️ name ⏩⏪ 🚫

operators
    +                                                                       ➕
    -                                                                       ➖
    /                                                                       ➗
    *                                                                       ✖️

    ==                                                                      🔎
    !=                                                                      ⛔🔎

    >                                                                       🐋 ?
    <                                                                       🐢 ?
    >=                                                                      🐬 ?
    <=                                                                      🐊 ?

    AND                                                                     🔗
    OR                                                                      ⛓️
    NOT                                                                     ⛔

conditional
    if_symbol conditional then body else_symbol body end_symbol             ❔ conditional 👉 ⏭️ ... ⏮️ ⭕ ⏭️ ... ⏮️ 🚫

loop
    loop_symbol conditional body end_symbol                                 🔄️ conditional ⏭️ ... ⏮️ 🚫

end_of_file                                                                 😴
