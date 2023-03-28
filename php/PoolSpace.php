<?php
class PoolSpace
{
  // Properties
  public $wallet;
  private $serialized_data;
  private $endpoint;

  function __construct($wallet)
  {
    $this->wallet = $wallet;
    $this->endpoint = 'https://api-mainnet.pool.space/api/farms/' . $wallet . '/';
    $this->serialized_data=json_decode(file_get_contents($this->endpoint));
  }

  // Methods
  function requestData()
  {
    return $this->serialized_data;
  }

  function unpaidBalance()
  {
    return $this->serialized_data->unpaidBalanceInXCH;
  }

  function totalPaidInXCH()
  {
    return $this->serialized_data->totalPaidInXCH;
  }

  function blocksFound()
  {
    return $this->serialized_data->blocksFound;
  }

  function estimatedPlotSizeTiB()
  {
    return $this->serialized_data->estimatedPlotSizeTiB;
  }

  function estimatedPlots()
  {
    return $this->serialized_data->estimatedPlots;
  }

  function pendingPoints()
  {
    return $this->serialized_data->pendingPoints;
  }

  function rank()
  {
    return $this->serialized_data->rank;
  }

  function globalPendingPoints(){
    return $this->serialized_data->globalPendingPoints;
  }

  function printAll(){
      foreach ($this->serialized_data as $key => $value) {
        if (is_array($value))
          print_r($value);
        else
          echo "$key ==> $value \n";
      }
    
    
  }
}