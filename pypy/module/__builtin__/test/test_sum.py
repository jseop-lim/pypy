class AppTestSum:

    def test_sum(self):
        raises(TypeError, sum, [b'a', b'c'], b'')
        raises(TypeError, sum, [bytearray(b'a'), bytearray(b'b')],
                bytearray(b''))
        raises(TypeError, sum, [[1], [2], [3]])
        raises(TypeError, sum, [{2:3}])
        raises(TypeError, sum, [{2:3}]*2, {2:3})

    def test_sum_iterates_before_checking_start(self):
        class IterRaises:
            def __iter__(self):
                raise RuntimeError
        raises(RuntimeError, sum, IterRaises(), '')
        raises(RuntimeError, sum, IterRaises(), b'')
        raises(RuntimeError, sum, IterRaises(), bytearray())
        raises(TypeError, sum, [], '')

    def test_sum_calls_iter_once(self):
        class OnlyNext:
            def __next__(self):
                raise StopIteration
        class Iterable:
            def __iter__(self):
                return OnlyNext()
        assert sum(Iterable(), 1j) == 1j
        assert sum(Iterable(), []) == []
        assert sum(Iterable(), ()) == ()
