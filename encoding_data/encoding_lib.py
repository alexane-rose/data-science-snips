import category_encoders as ce  # noqa: E402


def get_encoder(
    encoding_type, df, handle_unknown="return_nan", handle_missing="return_nan", n_components=20
):
    """This function generates returns a fitted encoder from the category encoder library.

    Arguments:
        ecoding_type: (str) Type of encoding. Either Binary, One_hot, Ordinal, or Hashing
        data: (pd.DataFrame) x_train data
        handle_unknown: (str) options are 'error', 'return_nan', 'value', and 'indicator'. The default is 'return_nan'
        handle_missing: (str) options are 'error', 'return_nan', 'value', and 'indicator'. The default is 'return_nan'
        n_components : (int) Used for hashing only, default is 20
    Returns:
        Encoding function
    """
    print(f"Encoding using {encoding_type} method")
    data = df.copy()
    category_columns = data.select_dtypes(
        include=["string", "object"]
    ).columns.to_list()

    print(f"Categorical columns : {category_columns}")
    data[category_columns] = data[category_columns].astype("category")

    if encoding_type.upper() == "BINARY":
        encoder = ce.BinaryEncoder(
            handle_unknown=handle_unknown, handle_missing=handle_missing
        )

    elif encoding_type.upper() == "ONE_HOT":
        encoder = ce.OneHotEncoder(
            handle_unknown=handle_unknown, handle_missing=handle_missing
        )

    elif encoding_type.upper() == "ORDINAL":
        encoder = ce.OrdinalEncoder(
            handle_unknown=handle_unknown, handle_missing=handle_missing
        )

    elif encoding_type.upper() == "HASHING":
        encoder = ce.HashingEncoder(n_components)

    else:
        raise Exception(
            "Wrong encoding type. Please choose either Binary, One_hot, Ordinal or Hashing"
        )

    return encoder.fit(data)
