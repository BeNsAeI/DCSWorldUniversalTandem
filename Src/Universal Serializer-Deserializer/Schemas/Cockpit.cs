namespace DCSWorldUniversalTandem.SerialDeserial
{
    using System;
    using System.Collections.Generic;

    using System.Globalization;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;

    public partial class Cockpit
    {
        [JsonProperty("seatName")]
        public string SeatName { get; set; }

        [JsonProperty("switches")]
        public List<Switch> Switches { get; set; }
    }
}