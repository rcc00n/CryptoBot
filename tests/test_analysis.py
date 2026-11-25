import unittest
import numpy as np
from logic import gauss_kernel, nadaraya_watson_envelope, find_signals

class AnalysisTests(unittest.TestCase):
    def test_constant_series_preserves_level_without_false_signals(self):
        series = np.full(7, 100.0)
        smooth, upper, lower = nadaraya_watson_envelope(series)
        np.testing.assert_allclose(smooth, series)
        np.testing.assert_allclose(upper, lower)
    def test_envelopes_order_and_kernel_symmetry(self):
        smooth, upper, lower = nadaraya_watson_envelope(np.array([1., 2., 5., 3., 4.]))
        self.assertTrue(np.all(upper >= smooth)); self.assertTrue(np.all(lower <= smooth))
        self.assertAlmostEqual(gauss_kernel(-2, 8), gauss_kernel(2, 8))
    def test_only_strict_outside_crossings_are_marked(self):
        buy, sell = find_signals(np.array([0., 1., 2., 3., 4.]), np.full(5, 3.), np.full(5, 1.))
        self.assertEqual(buy.tolist(), [True, False, False, False, False])
        self.assertEqual(sell.tolist(), [False, False, False, False, True])
