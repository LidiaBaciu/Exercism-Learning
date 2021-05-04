def slices(series, length):
    series_length = len(series)
    if series_length == 0 or length <= 0 or series_length < length:
        raise ValueError('not ok')
    result = []
    for i in range(0, series_length):
        if length + i <= series_length:
            result.append(series[i: length + i])
    return result