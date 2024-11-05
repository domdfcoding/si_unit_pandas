# stdlib
import operator

# 3rd party
import numpy  # type: ignore
import pandas  # type: ignore
import pandas.testing as tm  # type: ignore
import pytest
from pandas.core.generic import NDFrame  # type: ignore[import]

# this package
import si_unit_pandas


@pytest.fixture()
def series() -> pandas.Series:
	return pandas.Series(si_unit_pandas.TemperatureArray([0, 1, 2]))


@pytest.fixture()
def frame() -> pandas.DataFrame:
	return pandas.DataFrame({
			'A': si_unit_pandas.TemperatureArray([0, 1, 2]),
			'B': [0, 1, 2],
			'C': si_unit_pandas.TemperatureArray([0, 1, 2])
			})


@pytest.fixture(params=["series", "frame"])
def obj(request, series: pandas.Series, frame: pandas.DataFrame) -> NDFrame:
	if request.param == "series":
		return series
	elif request.param == "frame":
		return frame


# -----
# Tests
# -----
@pytest.mark.parametrize("method", [
		operator.methodcaller("head"),
		operator.methodcaller("rename", str),
		])
def test_works_generic(obj, method: operator.methodcaller):
	method(obj)


@pytest.mark.parametrize("method", [operator.methodcaller("info")])
def test_works_frame(frame: pandas.DataFrame, method: operator.methodcaller):
	method(frame)


def test__take(frame: pandas.DataFrame):
	return frame.take([0], axis=0)


def test_iloc_series(series: pandas.Series):
	series.iloc[slice(None)]
	series.iloc[0]
	series.iloc[[0]]
	series.iloc[[0, 1]]


def test_iloc_frame(frame: pandas.DataFrame):
	frame.iloc[:, 0]
	frame.iloc[:, [0]]
	frame.iloc[:, [0, 1]]
	frame.iloc[:, [0, 2]]

	frame.iloc[0, 0]
	frame.iloc[0, [0]]
	frame.iloc[0, [0, 1]]
	frame.iloc[0, [0, 2]]

	frame.iloc[[0], 0]
	frame.iloc[[0], [0]]
	frame.iloc[[0], [0, 1]]
	frame.iloc[[0], [0, 2]]


def test_loc_series(series: pandas.Series):
	series.loc[:]
	series.loc[0]
	series.loc[1]
	series.loc[[0, 1]]


def test_loc_frame(frame: pandas.DataFrame):
	frame.loc[:, 'A']
	frame.loc[:, ['A']]
	frame.loc[:, ['A', 'B']]
	frame.loc[:, ['A', 'C']]

	frame.loc[0, 'A']
	frame.loc[0, ['A']]
	frame.loc[0, ['A', 'B']]
	frame.loc[0, ['A', 'C']]

	frame.loc[[0], 'A']
	frame.loc[[0], ['A']]
	frame.loc[[0], ['A', 'B']]
	frame.loc[[0], ['A', 'C']]


def test_reindex(frame: pandas.DataFrame):
	result = frame.reindex([0, 10])
	expected = pandas.DataFrame({
			'A': si_unit_pandas.TemperatureArray([0, numpy.nan]),
			'B': [0, numpy.nan],
			'C': si_unit_pandas.TemperatureArray([0, numpy.nan])
			},
								index=[0, 10])
	tm.assert_frame_equal(result, expected)


def test_isna(series: pandas.Series):
	expected = pandas.Series([False, False, False], index=series.index, name=series.name)
	result = pandas.isna(series)
	tm.assert_series_equal(result, expected)

	result = series.isna()
	tm.assert_series_equal(result, expected)


def test_isna_frame(frame: pandas.DataFrame):
	result = frame.isna()
	expected = pandas.DataFrame({
			'A': [False, False, False],
			'B': [False, False, False],
			'C': [False, False, False],
			})
	tm.assert_frame_equal(result, expected)


def test_fillna():
	result = pandas.Series(si_unit_pandas.TemperatureArray([1, numpy.nan])).fillna(method="ffill")
	expected = pandas.Series(si_unit_pandas.TemperatureArray([1, 1]))
	tm.assert_series_equal(result, expected)


def test_dropna():
	missing = pandas.Series(si_unit_pandas.TemperatureArray([1, numpy.nan]))
	result = missing.dropna()
	expected = pandas.Series(si_unit_pandas.TemperatureArray([1]))
	tm.assert_series_equal(result, expected)

	result = missing.to_frame().dropna()
	expected = expected.to_frame()
	tm.assert_frame_equal(result, expected)
