import ctypes


def realpath(path):
    """
    Normalize a path using `GetFinalPathNameByHandleW` to get the
    path with all components in the case they exist in on-disk, so
    that making links to a case-sensitive server (hg.mozilla.org) works.

    This function also resolves any symlinks in the path.
    """
    # Return the original path if something fails, which can happen for paths that
    # don't exist on this system (like paths from the CRT).
    result = path

    ctypes.windll.kernel32.SetErrorMode(ctypes.c_uint(1))
    handle = ctypes.windll.kernel32.CreateFileW(
        path,
        # GENERIC_READ
        0x80000000,
        # FILE_SHARE_READ
        1,
        None,
        # OPEN_EXISTING
        3,
        # FILE_FLAG_BACKUP_SEMANTICS
        # This is necessary to open
        # directory handles.
        0x02000000,
        None,
    )
    if handle != -1:
        size = ctypes.windll.kernel32.GetFinalPathNameByHandleW(handle, None, 0, 0)
        buf = ctypes.create_unicode_buffer(size)
        if ctypes.windll.kernel32.GetFinalPathNameByHandleW(handle, buf, size, 0) > 0:
            # The return value of GetFinalPathNameByHandleW uses the
            # '\\?\' prefix.
            result = buf.value[4:]
        ctypes.windll.kernel32.CloseHandle(handle)
    return result

print(realpath("C:/Users/18463/Desktop/Folder"))
